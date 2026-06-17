from enum import StrEnum
from litestar.enums import HttpMethod, MediaType, OpenAPIMediaType, RequestEncodingType, ScopeType, ParamType, CompressionEncoding
from litestar.dto.field import Mark
from litestar.openapi.spec.enums import OpenAPIFormat, OpenAPIType

def test_enum_inheritance_strenum() -> None:
    # Ensure they are subclasses of StrEnum
    assert issubclass(HttpMethod, StrEnum)
    assert issubclass(MediaType, StrEnum)
    assert issubclass(OpenAPIMediaType, StrEnum)
    assert issubclass(RequestEncodingType, StrEnum)
    assert issubclass(ScopeType, StrEnum)
    assert issubclass(ParamType, StrEnum)
    assert issubclass(CompressionEncoding, StrEnum)
    assert issubclass(Mark, StrEnum)
    assert issubclass(OpenAPIFormat, StrEnum)
    assert issubclass(OpenAPIType, StrEnum)

def test_enum_string_comparison() -> None:
    # Ensure comparisons with plain strings work without TypeErrors
    assert HttpMethod.GET == "GET"
    assert HttpMethod.POST == "POST"
    assert MediaType.JSON == "application/json"
    assert Mark.READ_ONLY == "read-only"
    assert OpenAPIFormat.DATE == "date"
    assert OpenAPIType.STRING == "string"

    # Test comparison in list lookups
    methods = [HttpMethod.GET, HttpMethod.POST]
    assert "GET" in methods
    assert HttpMethod.GET in ["GET", "POST"]
