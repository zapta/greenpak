from pycparser import parse_file, c_parser, c_ast
import pycparser_fake_libc
import pycparser

fake_libc_arg = "-I" + pycparser_fake_libc.directory

def calculate_member_bits(decl):
    """Calculate the number of bits for a bitfield member."""
    # Check if this is a bitfield member by looking for a bitsize attribute
    if hasattr(decl, 'bitsize') and decl.bitsize is not None:
        # Extract the bitsize value as the number of bits this variable represents
        return int(decl.bitsize.value)
    else:
        # Handle standard unsigned types by checking the declaration type's name
        if hasattr(decl.type, 'type'):
            decl_type = decl.type.type
            if hasattr(decl_type, 'names'):
                type_name = ' '.join(decl_type.names)
                if type_name == 'uint8_t':
                    return 8
                elif type_name == 'uint16_t':
                    return 16
                elif type_name == 'uint32_t':
                    return 32
    # For non-bitfield members where the type is not one of the expected unsigned types,
    # or the type information is not available, return None
    return None

# Will do anonymous too
def print_struct_members_full(node, struct_name='', only_names=False):
    """Print the members of a struct or union."""
    if isinstance(node, (c_ast.Struct, c_ast.Union)) and node.decls:
        for decl in node.decls:
            if isinstance(decl.type, (c_ast.Struct, c_ast.Union)):
                #print(f"{'Struct' if isinstance(decl.type, c_ast.Struct) else 'Union'}:")
                print_struct_members(decl.type, only_names=only_names)
            else:
                # Print only the name if only_names is True, else print full details
                if only_names:
                    print(decl.name)
                else:
                    print(f"{decl.name}: {decl.type.__class__.__name__}")

def print_struct_members(node, member_names, only_names=False, suppress_output=False):
    """Print the members of a struct or union, skipping anonymous (unnamed) fields, and accumulate member names."""
    if isinstance(node, (c_ast.Struct, c_ast.Union)) and node.decls:
        for decl in node.decls:
            # if hasattr(decl, 'type'):
            #     print("Type:", type(decl.type))
            #     if hasattr(decl, 'bitsize') and decl.bitsize is not None:
            #         print("Bit Size:", decl.bitsize.value)
            # Check if it's an anonymous struct or union and recurse into it
            if isinstance(decl.type, (c_ast.Struct, c_ast.Union)) and not decl.name:
                # Pass the same member_names list to accumulate names from nested structures
                print_struct_members(decl.type, member_names, only_names=only_names, suppress_output=suppress_output)
            # Check if the declaration has a name before attempting to print it
            elif decl.name:
                #member_names.append(decl.name)  # Accumulate member names
                bits = calculate_member_bits(decl)
                member_names.append((decl.name,bits))
                if only_names and not suppress_output:
                    print(decl.name)
                elif not suppress_output:
                    print(f"{decl.name}: {decl.type.__class__.__name__}")
    return member_names


def visit_ast(filename, struct_name, only_names=False, suppress_output=False):
    """Visit AST of the given filename and print members of specified struct."""
    ast = parse_file(filename, use_cpp=True, cpp_path='gcc', cpp_args=['-E', fake_libc_arg])
    member_names = []
    for ext in ast.ext:
        # Check for Typedef or direct struct declarations that match the specified struct_name
        if isinstance(ext, c_ast.Typedef) and ext.name == struct_name:
            if not suppress_output:
                print(f"Struct Name: {ext.name}")
            member_names = print_struct_members(ext.type.type, member_names, only_names=only_names, suppress_output=suppress_output)
        elif isinstance(ext, c_ast.Decl) and isinstance(ext.type, c_ast.Struct) and ext.type.name == struct_name:
            if not suppress_output:
                print(f"Struct Name: {ext.name}")
            member_names = print_struct_members(ext.type, member_names, only_names=only_names, suppress_output=suppress_output)
    return member_names


def get_member_names(filename, struct_name):
    """Get the names of members of the specified struct."""
    return visit_ast(filename, struct_name, only_names=True, suppress_output=True)


def main():
    # Path to the preprocessed C header file
    #preprocessed_header_path = '/tmp/_slg46826_reg_t.h'

    #Note: passing un-preprocessed header
    header_path = 'c/slg46826_reg.h'

    #I want all of its elements, all named fields from this type
    struct_name = 'slg_register_t'

    member_names = visit_ast(header_path, struct_name, only_names=True)

    print(" ... filtering...")
    # Remote full array of 256 referene to.
    reg_and_bits_list = [name_bits_tuple for name_bits_tuple in member_names if name_bits_tuple[0] != 'reg_data']

    # Remove those pad-to-8bits tags
    reg_and_bits_list = [name_bits_tuple for name_bits_tuple in reg_and_bits_list if not name_bits_tuple[0].startswith('pad_')]

    for member_name, bits in reg_and_bits_list:
        print(f"{member_name}: {bits} bits")


if __name__ == "__main__":
    main()
