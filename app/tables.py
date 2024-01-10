from pynamodb.attributes import NumberAttribute, UnicodeAttribute
from pynamodb.indexes import AllProjection, GlobalSecondaryIndex
from pynamodb.models import Model

from .config import settings


class BaseTable(Model):
    class Meta:
        host = settings.DB_HOST if config.ENVIRONMENT in ["local", "test"] else None
        region = settings.DB_REGION_NAME


class ProductNameIndex(GlobalSecondaryIndex["ProductTable"]):
    """
    Represents a global secondary index for ProductTable
    """

    class Meta:
        index_name = "product-name-index"
        read_capacity_units = 10
        write_capacity_units = 10
        projection = AllProjection()

    name = UnicodeAttribute(hash_key=True)
    updated_at = NumberAttribute(range_key=True)


class ProductTable(BaseTable):
    """
    Represents a DynamoDB table for a Product
    """

    class Meta(BaseTable.Meta):
        table_name = "product-table"

    id = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=False)
    created_at = NumberAttribute(null=False)
    updated_at = NumberAttribute(null=False)

    product_name_index = ProductNameIndex()