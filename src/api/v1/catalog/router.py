from fastapi import APIRouter

catalog_router = APIRouter()


@catalog_router.get("/products")
async def get_products():
    """Get all products"""
    return {
        "products": [
            {"id": 1, "name": "Product 1", "price": 100},
            {"id": 2, "name": "Product 2", "price": 200},
            {"id": 3, "name": "Product 3", "price": 300}
        ]
    }


@catalog_router.get("/products/{product_id}")
async def get_product(product_id: int):
    """Get product by ID"""
    return {"id": product_id, "name": f"Product {product_id}", "price": product_id * 100}


@catalog_router.get("/categories")
async def get_categories():
    """Get all categories"""
    return {
        "categories": [
            {"id": 1, "name": "Electronics"},
            {"id": 2, "name": "Clothing"},
            {"id": 3, "name": "Books"}
        ]
    }


@catalog_router.get("/categories/{category_id}/products")
async def get_products_by_category(category_id: int):
    """Get products by category"""
    return {
        "category_id": category_id,
        "products": [
            {"id": 1, "name": f"Product in category {category_id}", "price": 100}
        ]
    } 