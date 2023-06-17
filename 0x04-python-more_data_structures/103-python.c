#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

/**
 * print_python_bytes - prints info related to Python lists
 *
 * @p: a pointer of Python object.
 *
 * Return: Nothing.
 */
void print_python_bytes(PyObject *p)
{
	long int size_p;
	int index;
	char *get_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &get_str, &size);

	printf("  size_p: %li\n", size_p);
	printf("  trying string: %s\n", get_str);
	if (size_p < 10)
		printf("  first %li bytes:", size_p + 1);
	else
		printf("  first 10 bytes:");
	for (index = 0; index <= size_p && index < 10; index++)
		printf(" %02hhx", get_str[index]);
	printf("\n");
}


/**
 * print_python_list - prints info related to Python bytes
 *
 * @p: a pointer of Python object.
 *
 * Return: Nothing.
 */
void print_python_list(PyObject *p)
{
	long int size_p = PyList_Size(p);
	int index;
	PyListObject *list = (PyListObject *)p;
	const char *type;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", size_p);
	printf("[*] Allocated = %li\n", list->allocated);
	for (index = 0; index < size_p; index++)
	{
		type = (list->obj_item[index])->obj_type->tp_name;
		printf("Element %i: %s\n", index, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(list->obj_item[index]);
	}
}
