def uleb128_value(data, off): 
	size = 1
	result = data[off+0]
	if result > 0x7f :
		cur = data[off+1]
		result = (result & 0x7f) | ((cur & 0x7f) << 7)
		size += 1
		if cur > 0x7f :
			cur = data[off+2]
			result |= ((cur & 0x7f) << 14) 
			size += 1
			if cur > 0x7f :
				cur = data[off+3]
				result |= ((cur & 0x7f) << 21) 
				size += 1
				if cur > 0x7f :
					cur = data[off+4]
					result |= (cur << 28)
					size += 1

	return result, size


def encoded_field(data, offset):
	myoff = offset

	field_idx_diff, size = uleb128_value(data, myoff)
	myoff += size
	access_flags, size = uleb128_value(data, myoff)
	myoff += size

	size = myoff - offset

	return [field_idx_diff, access_flags, size]


def encoded_method(data, offset):
	myoff = offset

	method_idx_diff, size = uleb128_value(data, myoff)
	myoff += size
	access_flags, size = uleb128_value(data, myoff)
	myoff += size
	code_off, size = uleb128_value(data, myoff)
	myoff += size

	size = myoff - offset

	return [method_idx_diff, access_flags, code_off, size]


def encoded_annotation(data, offset):
	myoff = offset

	type_idx_diff, size = uleb128_value(data, myoff)
	myoff += size
	size_diff, size = uleb128_value(data, myoff)
	myoff += size
	name_idx_diff, size = uleb128_value(data, myoff)
	myoff += size
	value_type = data[myoff:myoff+1]
	encoded_value = data[myoff+1:myoff+2]

	return [type_idx_diff, size_diff, name_idx_diff, value_type, encoded_value]
