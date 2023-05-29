#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *item;

    if (!PyList_Check(p))
    {
        printf("[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
    }
}

void print_python_bytes(PyObject *p)
{
    Py_ssize_t size, i;
    char *string;

    if (!PyBytes_Check(p))
    {
        printf("[.] bytes object info\n  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    string = PyBytes_AsString(p);

    printf("[.] bytes object info\n  size: %ld\n", size);
    printf("  trying string: %s\n", string);

    if (size > 10)
        size = 10;

    printf("  first %ld bytes:", size);
    for (i = 0; i < size; i++)
        printf(" %02x", (unsigned char)string[i]);

    printf("\n");
}

void print_python_float(PyObject *p)
{
    double value;

    if (!PyFloat_Check(p))
    {
        printf("[.] float object info\n  [ERROR] Invalid Float Object\n");
        return;
    }

    value = PyFloat_AsDouble(p);

    printf("[.] float object info\n  value: %f\n", value);
}
