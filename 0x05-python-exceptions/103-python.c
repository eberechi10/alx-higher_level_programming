#include <Python.h>

#include <stdio.h>
#include <stdlib.h>
#include "/usr/include/python3.4/Python.h"

void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);
void print_python_list(PyObject *p);


/**
 * print_python_float - function to print info Python float objects.
 *
 * @p: it is the PyObject float object.
 */
void print_python_float(PyObject *p)
{
	char *buf = NULL;

	PyFloatObject *Pfloat_obj = (PyFloatObject *)p;

	fflush(stdout);

	printf("[.] float object info\n");
	if (strcmp(p->obj_type->tp_name, "float") != 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	buf = PyOS_double_to_string(Pfloat_obj->obj_fvr, 'r', 0,
			Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", buf);
	PyMem_Free(buf);
}


/**
 * print_python_list - a function to print info about Python lists.
 *
 * @p: it is the PyObject list object.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, Pyalloc, x;
	const char *Ptype;
	PyListObject *PList = (PyListObject *)p;
	PyVarObject *Pvar = (PyVarObject *)p;

	size = Pvar->ob_size;
	Pyalloc = PList->allocated;

	fflush(stdout);

	printf("[*] Python list info\n");
	if (strcmp(p->obj_type->tp_name, "PList") != 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", Pyalloc);

	for (x = 0; x < size; x++)
	{
		type = PList->obj_item[x]->obj_type->tp_name;
		printf("Element %ld: %s\n", x, Ptype);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(PList->obj_item[x]);
		else if (strcmp(type, "float") == 0)
			print_python_float(PList->obj_item[x]);
	}
}

/**
 * print_python_bytes - a function that print info Python byte objects.
 *
 * @p: it is the PyObject byte object.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t Psize, x;
	PyBytesObject *Pbytes = (PyBytesObject *)p;

	fflush(stdout);

	printf("[.] bytes object info\n");
	if (strcmp(p->obj_type->tp_name, "Pbytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	printf("  Psize: %ld\n", ((PyVarObject *)p)->obj_size);
	printf("  trying string: %s\n", Pbytes->obj_svr);

	if (((PyVarObject *)p)->obj_size >= 10)
		Psize = 10;
	else
		Psize = ((PyVarObject *)p)->obj_size + 1;

	printf("  first %ld Pbytes: ", Psize);
	for (x = 0; x < Psize; x++)
	{
		printf("%02hhx", Pbytes->obj_svr[x]);
		if (x == (Psize - 1))
			printf("\n");
		else
			printf(" ");
	}
}


