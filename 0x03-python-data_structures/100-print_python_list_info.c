#include <stdio.h>
#include <python.h>


/**
 * print_python_list_info - prints info related to Python lists
 * @p: the Pointer to Python object.
 *
 * Return: void.
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	PyObject *item_py;
	long int size = Py_SIZE(p), x;
	const char *i_Type
	
	list = (PyListObject *)p;

	printf("[*] Size of the Python List = %ld\n", size);

	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < size; x++)
	{
		item_py = PyList_GetItem(p, x);
		i_Type = Py_TYPE(item_py)->tp_name;
		printf("Element %ld: %s\n", x, i_Type);
	}
}
