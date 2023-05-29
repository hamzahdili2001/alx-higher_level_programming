#include <Python.h>
#include <stdio.h>
#include <stdlib.h>

void print_python_float(PyObject *p)
{
	double d;
	char *str = NULL;

	printf("[.] float object info\n");

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	d = PyFloat_AS_DOUBLE(p);
	str = PyOS_double_to_string(d, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	if (str != NULL)
	{
		printf("  value: %s\n", str);
		PyMem_Free(str);
	}
}

void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *str;

	printf("[.] bytes object info\n");

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_GET_SIZE(p);
	str = PyBytes_AS_STRING(p);

	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", str);

	printf("  first %zd bytes:", (size <= 10) ? size : 10);
	for (i = 0; i < ((size <= 10) ? size : 10); i++)
		printf(" %02x", (unsigned char)str[i]);

	printf("\n");
}

void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list info\n");

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	size = PyList_GET_SIZE(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);

		if (PyBytes_Check(item))
			print_python_bytes(item);
		else if (PyFloat_Check(item))
			print_python_float(item);
	}
}

