from django.template.defaulttags import register
import json

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

def conv_data_enum(datastring, datafield, jsonconf):
    datastring = str(datastring)
    if 'enumFields' in jsonconf[datafield]:
        return jsonconf[datafield]['enumFields'][datastring] if datastring in jsonconf[datafield]['enumFields'] else f"--INVALID ENUM: {datastring} {len(datastring)}"
    return datastring

@register.filter
def enum_data1_string(datastring, jsonconf):
    return conv_data_enum(datastring, 'data1', jsonconf)

@register.filter
def enum_data2_string(datastring, jsonconf):
    return conv_data_enum(datastring, 'data2', jsonconf)

@register.filter
def enum_data3_string(datastring, jsonconf):
    return conv_data_enum(datastring, 'data3', jsonconf)

@register.filter
def enum_data4_string(datastring, jsonconf):
    return conv_data_enum(datastring, 'data4', jsonconf)