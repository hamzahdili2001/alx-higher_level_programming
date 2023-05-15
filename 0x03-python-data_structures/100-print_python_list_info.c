#include <stdio.h>
#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/object.h"
#include "/usr/include/python3.4/listobject.h"
/**
 * print_python_list_info - function that prints some basic
 *													info about Python lists
 * @p: object
 * Return: Nothing.
*/
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p), i = 0;
	PyListObject *copy = (PyListObject *) p;
	PyObject *t;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", (int)copy->allocated);

	while (i < size)
	{
		t = PyList_GET_ITEM(p, i);
		printf("Element %d: %s\n", i, t->ob_type->tp_name);
		i++;
	}
}
