from fastapi import APIRouter, HTTPException, status
from schemas.item_schema import ItemCreate, ItemUpdate, ItemResponse
from crud.items import create_item, get_item_by_id, update_item, delete_item, filter_items, count_items_by_email

router = APIRouter()

@router.post(
    "/",
    response_model=ItemResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create a New Item",
    description="Create a new item with the provided details. Automatically inserts the current date as the insert date.",
)
async def create_item_endpoint(item: ItemCreate):
    item_id = await create_item(item.dict())
    created_item = await get_item_by_id(item_id)

    # Rename `_id` to `id` for the response
    created_item['id'] = created_item.pop('_id')  # Rename _id to id

    return created_item

@router.get("/{id}", response_model=ItemResponse, summary="Get Item by ID")
async def read_item(item_id: str):
    item = await get_item_by_id(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Rename `_id` to `id` for the response
    item['id'] = item.pop('_id')  # Rename _id to id

    return item

@router.put("/{id}", response_model=ItemResponse, summary="Update an Item by ID")
async def update_item_endpoint(item_id: str, item: ItemUpdate):
    updated = await update_item(item_id, item.dict(exclude_unset=True))
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return await read_item(item_id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete an Item by ID")
async def delete_item_endpoint(item_id: str):
    deleted = await delete_item(item_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return

@router.get("/filter", response_model=list[ItemResponse], summary="Filter Items")
async def filter_items_endpoint(email: str = None, expiry_date: str = None, insert_date: str = None, quantity: int = None):
    filters = {}
    if email:
        filters["email"] = email
    if expiry_date:
        filters["expiry_date"] = expiry_date
    if insert_date:
        filters["insert_date"] = insert_date
    if quantity:
        filters["quantity"] = quantity
    items = await filter_items(filters)
    for item in items:
        item['id'] = item.pop('_id')  # Rename _id to id in filtered items
    return items

@router.get("/count", summary="Count Items by Email")
async def count_items_endpoint():
    counts = await count_items_by_email()  # Call the async function correctly
    return counts