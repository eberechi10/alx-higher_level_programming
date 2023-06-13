#include "lists.h"
#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/object.h"
#include "/usr/include/python3.4/listobject.h"

/**
 * print_python_list_info - prints info to the lists
 * @p: Pointer to object.
 *
 * Return: Nothing.
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;
	Py_ssize_t x;
	PyObject *i_Obj;
	const char *i_Type;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (x = 0; x < size; x++)
	{
		i_Obj = PyList_GetItem(p, x);
		i_Type = Py_TYPE(i_Obj)->tp_name;
		printf("Element %ld: %s\n", x, i_Type);
	}
}
