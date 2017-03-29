from docsnippet import DocSnippet
# Define a docsnippet for testing purposes

test_function_name = "cool_function"
test_parameter_names = ["foo", "bar"]
test_return_name = "retour"
test_function_comment = "Some amazingly awesome documentation about cool_functions that features foo, bar and retodur"

my_snippet = DocSnippet()
my_snippet.create(function_name = test_function_name,
                  parameter_names = test_parameter_names,
                  return_name = test_return_name,
                  function_comment = test_function_comment)



if my_snippet.covers_function():
    print("We found " + str(test_function_name) + "in the source code comment: " + str(test_function_comment))
else:
    print("No " + str(test_function_name) + " found in source code comment.")

if my_snippet.covers_parameters():
    print("We found " + str(test_parameter_names) + "in the source code comment: " + str(test_function_comment))
else:
    print("No " + str(test_parameter_names) + " found in source code comment.")

print(my_snippet.get_score())


#def test_answer():
#    assert docsnippet.get_score() == 0
