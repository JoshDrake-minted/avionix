from typing import List, Optional, Union

from avionix.yaml.yaml_handling import HelmYaml


class JSONSchemaPropsOrArray(HelmYaml):
    """
    """

    pass


class ExternalDocumentation(HelmYaml):
    """
    :param description:None
    :type description: str
    :param url:None
    :type url: str
    """

    def __init__(self, description: str, url: str):
        self.description = description
        self.url = url


class JSONSchemaPropsOrBool(HelmYaml):
    """
    """

    pass


class JSON(HelmYaml):
    """
    """

    pass


class JSONSchemaProps(HelmYaml):
    """
    :param additional_items:None
    :type additional_items: JSONSchemaPropsOrBool
    :param additional_properties:None
    :type additional_properties: JSONSchemaPropsOrBool
    :param all_of:None
    :type all_of: List["JSONSchemaProps"]
    :param any_of:None
    :type any_of: List["JSONSchemaProps"]
    :param definitions:None
    :type definitions: dict
    :param dependencies:None
    :type dependencies: dict
    :param description:None
    :type description: str
    :param enum:None
    :type enum: List[JSON]
    :param example:None
    :type example: JSON
    :param exclusive_maximum:None
    :type exclusive_maximum: bool
    :param exclusive_minimum:None
    :type exclusive_minimum: bool
    :param external_docs:None
    :type external_docs: ExternalDocumentation
    :param format:format is an OpenAPI v3 format string. Unknown formats are ignored. \
        The following formats are validated:  - bsonobjectid: a bson object ID, i.e. a \
        24 characters hex string - uri: an URI as parsed by Golang \
        net/url.ParseRequestURI - email: an email address as parsed by Golang \
        net/mail.ParseAddress - hostname: a valid representation for an Internet host \
        name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as \
        parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang \
        net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC \
        address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase \
        defined by the regex \
        (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - \
        uuid3: an UUID3 that allows uppercase defined by the regex \
        (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - \
        uuid4: an UUID4 that allows uppercase defined by the regex \
        (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ \
        - uuid5: an UUID5 that allows uppercase defined by the regex \
        (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ \
        - isbn: an ISBN10 or ISBN13 number string like "0321751043" or \
        "978-0321751041" - isbn10: an ISBN10 number string like "0321751043" - isbn13: \
        an ISBN13 number string like "978-0321751041" - creditcard: a credit card \
        number defined by the regex \
        ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\d{3})\d{11})$  # noqa \
        with any non digit characters mixed in - ssn: a U.S. social security number \
        following the regex ^\d{3}[- ]?\d{2}[- ]?\d{4}$ - hexcolor: an hexadecimal \
        color code like "#FFFFFF: following the regex \
        ^#?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb \
        like "rgb(255,255,2559" - byte: base64 encoded binary data - password: any \
        kind of string - date: a date string like "2006-01-02" as defined by full-date \
        in RFC3339 - duration: a duration string like "22 ns" as parsed by Golang \
        time.ParseDuration or compatible with Scala duration format - datetime: a date \
        time string like "2014-12-15T19:30:20.000Z" as defined by date-time in \
        RFC3339.
    :type format: str
    :param id:None
    :type id: str
    :param items:None
    :type items: JSONSchemaPropsOrArray
    :param max_items:None
    :type max_items: int
    :param max_length:None
    :type max_length: int
    :param max_properties:None
    :type max_properties: int
    :param maximum:None
    :type maximum: Union[int, float]
    :param min_items:None
    :type min_items: int
    :param min_length:None
    :type min_length: int
    :param min_properties:None
    :type min_properties: int
    :param minimum:None
    :type minimum: Union[int, float]
    :param multiple_of:None
    :type multiple_of: Union[int, float]
    :param not_:None
    :type not_: "JSONSchemaProps"
    :param nullable:None
    :type nullable: bool
    :param one_of:None
    :type one_of: List["JSONSchemaProps"]
    :param pattern:None
    :type pattern: str
    :param pattern_properties:None
    :type pattern_properties: dict
    :param properties:None
    :type properties: dict
    :param required:None
    :type required: List[str]
    :param title:None
    :type title: str
    :param type:None
    :type type: str
    :param unique_items:None
    :type unique_items: bool
    :param x_kubernetes_embedded_resource:x-kubernetes-embedded-resource defines that \
        the value is an embedded Kubernetes runtime.Object, with TypeMeta and \
        ObjectMeta. The type must be object. It is allowed to further restrict the \
        embedded object. kind, apiVersion and metadata are validated automatically. \
        x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have \
        to be if the object is fully specified (up to kind, apiVersion, metadata).
    :type x_kubernetes_embedded_resource: bool
    :param x_kubernetes_int_or_string:x-kubernetes-int-or-string specifies that this \
        value is either an integer or a string. If this is true, an empty type is \
        allowed and type as child of anyOf is permitted if following one of the \
        following patterns:  1) anyOf:    - type: integer    - type: string 2) allOf:  \
          - anyOf:      - type: integer      - type: string    - ... zero or more
    :type x_kubernetes_int_or_string: bool
    :param x_kubernetes_list_map_keys:x-kubernetes-list-map-keys annotates an array \
        with the x-kubernetes-list-type `map` by specifying the keys used as the index \
        of the map.  This tag MUST only be used on lists that have the \
        "x-kubernetes-list-type" extension set to "map". Also, the values specified \
        for this attribute must be a scalar typed field of the child structure (no \
        nesting is supported).  The properties specified must either be required or \
        have a default value, to ensure those properties are present for all list \
        items.
    :type x_kubernetes_list_map_keys: List[str]
    :param x_kubernetes_map_type:x-kubernetes-map-type annotates an object to further \
        describe its topology. This extension must only be used when type is object \
        and may have 2 possible values:  1) `granular`:      These maps are actual \
        maps (key-value pairs) and each fields are independent      from each other \
        (they can each be manipulated by separate actors). This is      the default \
        behaviour for all maps. 2) `atomic`: the list is treated as a single entity, \
        like a scalar.      Atomic maps will be entirely replaced when updated.
    :type x_kubernetes_map_type: str
    :param x_kubernetes_preserve_unknown_fields:x-kubernetes-preserve-unknown-fields \
        stops the API server decoding step from pruning fields which are not specified \
        in the validation schema. This affects fields recursively, but switches back \
        to normal pruning behaviour if nested properties or additionalProperties are \
        specified in the schema. This can either be true or undefined. False is \
        forbidden.
    :type x_kubernetes_preserve_unknown_fields: bool
    :param default:default is a default value for undefined object fields. Defaulting \
        is a beta feature under the CustomResourceDefaulting feature gate. Defaulting \
        requires spec.preserveUnknownFields to be false.
    :type default: Optional[JSON]
    :param x_kubernetes_list_type:x-kubernetes-list-type annotates an array to further \
        describe its topology. This extension must only be used on lists and may have \
        3 possible values:  1) `atomic`: the list is treated as a single entity, like \
        a scalar.      Atomic lists will be entirely replaced when updated. This \
        extension      may be used on any type of list (struct, scalar, ...). 2) \
        `set`:      Sets are lists that must not have multiple items with the same \
        value. Each      value must be a scalar, an object with x-kubernetes-map-type \
        `atomic` or an      array with x-kubernetes-list-type `atomic`. 3) `map`:      \
        These lists are like maps in that their elements have a non-index key      \
        used to identify them. Order is preserved upon merge. The map tag      must \
        only be used on a list with elements of type object. Defaults to atomic for \
        arrays.
    :type x_kubernetes_list_type: Optional[str]
    """

    def __init__(
        self,
        type: str,
        additional_items: Optional[JSONSchemaPropsOrBool] = None,
        additional_properties: Optional[JSONSchemaPropsOrBool] = None,
        all_of: Optional[List["JSONSchemaProps"]] = None,
        any_of: Optional[List["JSONSchemaProps"]] = None,
        definitions: Optional[dict] = None,
        dependencies: Optional[dict] = None,
        description: Optional[str] = None,
        enum: Optional[List[JSON]] = None,
        example: Optional[JSON] = None,
        exclusive_maximum: Optional[bool] = None,
        exclusive_minimum: Optional[bool] = None,
        external_docs: Optional[ExternalDocumentation] = None,
        format: Optional[str] = None,
        id: Optional[str] = None,
        items: Optional[JSONSchemaPropsOrArray] = None,
        max_items: Optional[int] = None,
        max_length: Optional[int] = None,
        max_properties: Optional[int] = None,
        maximum: Optional[Union[int, float]] = None,
        min_items: Optional[int] = None,
        min_length: Optional[int] = None,
        min_properties: Optional[int] = None,
        minimum: Optional[Union[int, float]] = None,
        multiple_of: Optional[Union[int, float]] = None,
        not_: Optional["JSONSchemaProps"] = None,
        nullable: Optional[bool] = None,
        one_of: Optional[List["JSONSchemaProps"]] = None,
        pattern: Optional[str] = None,
        pattern_properties: Optional[dict] = None,
        properties: Optional[dict] = None,
        required: Optional[List[str]] = None,
        title: Optional[str] = None,
        unique_items: Optional[bool] = None,
        x_kubernetes_embedded_resource: Optional[bool] = None,
        x_kubernetes_int_or_string: Optional[bool] = None,
        x_kubernetes_list_map_keys: Optional[List[str]] = None,
        x_kubernetes_map_type: Optional[str] = None,
        x_kubernetes_preserve_unknown_fields: Optional[bool] = None,
        default: Optional[JSON] = None,
        x_kubernetes_list_type: Optional[str] = None,
    ):
        self.additionalItems = additional_items
        self.additionalProperties = additional_properties
        self.allOf = all_of
        self.anyOf = any_of
        self.definitions = definitions
        self.dependencies = dependencies
        self.description = description
        self.enum = enum
        self.example = example
        self.exclusiveMaximum = exclusive_maximum
        self.exclusiveMinimum = exclusive_minimum
        self.externalDocs = external_docs
        self.format = format
        self.id = id
        self.items = items
        self.maxItems = max_items
        self.maxLength = max_length
        self.maxProperties = max_properties
        self.maximum = maximum
        self.minItems = min_items
        self.minLength = min_length
        self.minProperties = min_properties
        self.minimum = minimum
        self.multipleOf = multiple_of
        self["not"] = not_
        self.nullable = nullable
        self.oneOf = one_of
        self.pattern = pattern
        self.patternProperties = pattern_properties
        self.properties = properties
        self.required = required
        self.title = title
        self.type = type
        self.uniqueItems = unique_items
        self["x-kubernetes-embedded-resource"] = x_kubernetes_embedded_resource
        self["x-kubernetes-int-or-string"] = x_kubernetes_int_or_string
        self["x-kubernetes-list-map-keys"] = x_kubernetes_list_map_keys
        self["x-kubernetes-map-type"] = x_kubernetes_map_type
        self[
            "x-kubernetes-preserve-unknown-fields"
        ] = x_kubernetes_preserve_unknown_fields
        self.default = default
        self["x-kubernetes-list-type"] = x_kubernetes_list_type
