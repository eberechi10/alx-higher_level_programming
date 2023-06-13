#include <Python.h>
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
	PyListObject *list;
	Py_ssize_t size, x;
	PyObject *object;
	struct _typeobject *type;

	if (strcmp(p->obj_type->tp_name, "list") == 0)
	{
		list = (PyListObject *)p;
		size = list->obj_base.obj_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (x = 0; x < size; x++)
		{
			object = list->obj_item[x];
			type = object->obj_type;
			printf("Element %ld: %s\n", x, type->tp_name);
		}
	}
}
