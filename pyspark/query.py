import pyspark

def get_products(products_df, categories_df):
    """
    We have to join products and categories on product name then select product
    and category names and show distinct couples
    """
    result_df = products_df.join(categories_df, products_df["product_name"] == categories_df["product_name"], "left")
    result_df = result_df.select(products_df["product_name"], categories_df["category_name"]).distinct()
    result_df.show()
