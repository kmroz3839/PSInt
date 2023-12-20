from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def gamedetails_enum_string(num_value: int, field_name: str, game_config: str):
    game = json.loads(game_config)
    if game[field_name]["enum_fields"] is not None:
        return game[field_name]["enum_fields"][num_value]
    return num_value
