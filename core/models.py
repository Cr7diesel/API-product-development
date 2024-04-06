import uuid
from . import database as db

from sqlalchemy import (
    Column,
    Boolean,
    DateTime,
    DECIMAL,
    Float,
    Integer,
    ForeignKey,
    String,
    Text,
    text,
)
from sqlalchemy.dialects.postgresql import UUID


class Category(db.Model):

    __tablename__ = "category"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True, nullable=False)
    slug = Column(String(200), unique=True, nullable=False)
    is_active = Column(Boolean, default=False)
    parent_id = Column(Integer, ForeignKey("category.id"))

    def __repr__(self) -> str:
        return f"<Name: {self.name}>"


class Product(db.Model):

    __tablename__ = "product"

    id = Column(Integer, primary_key=True)
    pid = Column(
        UUID(as_uuid=True),
        unique=True,
        nullable=False,
        server_default=text("uuid_generate_v4()"),
    )
    name = Column(String(200), unique=True, nullable=False)
    slug = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    is_digital = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    updated_at = Column(
        DateTime, server_default=db.text("CURRENT_TIMESTAMP"), onupdate=db.func.now()
    )
    is_active = Column(Boolean, default=False)
    stock_status = Column(String(100), default="OUT_OF_STOCK")
    category_id = Column(Integer, ForeignKey="category.id")
    seasonal_events_id = Column(
        Integer, ForeignKey=('seasonal_events.id')
    )

    def __repr__(self) -> str:
        return f"<Name: {self.name}>"


class ProductLine(db.Model):

    __tablename__ = "product_line"

    id = Column(Integer, primary_key=True)
    price = Column(DECIMAL(5, 2))
    sku = Column(UUID(as_uuid=True), default=uuid.uuid4)
    stock_qty = Column(Integer, default=0)
    is_active = Column(Boolean, default=False)
    order = Column(Integer)
    weight = Column(Float)
    created_at = Column(DateTime, server_default=db.text("CURRENT_TIMESTAMP"))
    product_id = Column(Integer, ForeignKey="product.id")

    def __repr__(self) -> str:
        return f"ProductLine: {self.id}"


class ProductImage(db.Model):

    __tablename__ = "product_image"

    id = Column(Integer, primary_key=True)
    alternative_text = Column(String(255))
    url = Column(String(255))
    order = Column(Integer)
    product_line_id = Column(Integer, ForeignKey="product_line.id")

    def __repr__(self) -> str:
        return f"ProductImage: {self.id}"


class SeasonalEvents(db.Model):

    __tablename__ = "seasonal_events"

    id = Column(Integer, primary_key=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    name = Column(String(100), unique=True)

    def __repr__(self) -> str:
        return self.name
