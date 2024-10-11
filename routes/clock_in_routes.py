from fastapi import APIRouter, HTTPException, status
from schemas.clock_in_schema import ClockInCreate, ClockInUpdate, ClockInResponse, ClockInRequest
from crud.clock_in_records import create_clock_in, get_clock_in_by_id, update_clock_in, delete_clock_in, filter_clock_ins
from typing import Optional

router = APIRouter()

@router.post("/", response_model=ClockInResponse, status_code=status.HTTP_201_CREATED)
async def clock_in_endpoint(clock_in_data: ClockInRequest):
    created_clock_in = await create_clock_in(clock_in_data.dict())
    return created_clock_in  # Return the complete data

@router.get("/{id}", response_model=ClockInResponse, summary="Get Clock-In by ID")
async def read_clock_in(clock_in_id: str):
    clock_in = await get_clock_in_by_id(clock_in_id)
    if not clock_in:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return clock_in

@router.put("/{clock_in_id}", response_model=ClockInResponse, summary="Update a Clock-In by ID")
async def update_clock_in_endpoint(clock_in_id: str, clock_in: ClockInUpdate):
    updated = await update_clock_in(clock_in_id, clock_in.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return await get_clock_in_by_id(clock_in_id)

@router.delete("/{clock_in_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a Clock-In by ID")
async def delete_clock_in_endpoint(clock_in_id: str):
    deleted = await delete_clock_in(clock_in_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Clock-in record not found")
    return

@router.get("/filter", response_model=list[ClockInResponse], summary="Filter Clock-Ins")
async def filter_clock_ins_endpoint(
    email: Optional[str] = None,
    location: Optional[str] = None,
    insert_datetime: Optional[str] = None,
):
    filters = {}
    if email:
        filters["email"] = email
    if location:
        filters["location"] = location
    if insert_datetime:
        filters["insert_datetime"] = insert_datetime

    clock_ins = await filter_clock_ins(filters)
    return clock_ins