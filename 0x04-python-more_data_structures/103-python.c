#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include "/usr/include/python3.4/Python.h"
#include <stdio.h>


/**
 * print_python_list - prints info related to Python bytes
 *
 * @p: a pointer of Python object.
 *
 * Return: Nothing.
 */

void print_python_list(PyObject *p)
{
	int index, size_p, elm;
	PyListObject *py_list = (PyListObject *)p;
	PyVarObject *pyvar = (PyVarObject *)p;
	const char *type;

	size_p = pvar->obj_size;
	elm = py_list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size_p);
	printf("[*] Allocated = %d\n", elm);

	for (index = 0; index < size_p; index++)
	{
		type = py_list->obj_item[index]->obj_type->tp_name;
		printf("Element %d: %s\n", index, type);
		if (!strcmp(type, "bytes"))
			print_python_bytes(py_list->obj_item[index]);
	}
}

/**
 * print_python_bytes - prints info related to Python lists
 *
 * @p: a pointer of Python object.
 *
 * Return: Nothing.
 */

void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	unsigned char index, size_p;

	printf("[.] bytes object info\n");
	if (strcmp(p->obj_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  size_p: %ld\n", ((PyVarObject *)p)->obj_size);
	printf("  trying string: %s\n", bytes->obj_sval);

	if (((PyVarObject *)p)->obj_size > 10)
		size_p = 10;
	else
		size_P = ((PyVarObject *)p)->obj_size + 1;

	printf("  first %d bytes: ", size_p);
	for (index = 0; index < size_p; index++)
	{
		printf("%02hhx", bytes->obj_sval[index]);
		if (index == (size_p - 1))
			printf("\n");
		else
			printf(" ");
	}
}
