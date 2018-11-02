# 17-Oct-2018: Intro to python

## basic programming concepts:

* Python uses dot notation: `object.method` so **Don't** use dots in variable
names.

* **0 indexed**: `data[0:5]`= values of `data` up to but **not including** 5, i.e. 5 elements: (5 - 0 = 5)

```python
>>> data=(0,1,2,3,4,5)
>>> data[0:5]
(0, 1, 2, 3, 4)
>>>
```

* `-N` is used to index the Nth value from the end

```python
>>> data[-1]
5
```

## SWC - Programming with python:

http://swcarpentry.github.io/python-novice-inflammation/01-numpy/

* Assigning variables and calling them are done similarly to R.

```python
weight_kg = 60
print(weight_kg)
```

```
60
```

Variables can't start with numbers or have spaces (Also: don't use dots)

* `numpy` library can read text files with the `numpy.loadtxt(fname, delimiter)` function.

```python
data = numpy.loadtxt(fname='data/inflammation-01.csv', delimiter=',')
print(type(data))
```

```
<class 'numpy.ndarray'>
```

```python
print(data.dtype)
```

```
'float64'
```

* python can assign multiple things on one line

```python
maxval, minval, stdval = numpy.max(data), numpy.min(data), numpy.std(data)

minval
```

```
0.0
```

* most array functions have an axis argument. For example `numpy.mean()` can
take the row average or column average:

```python
# row averages - axis=1 would be column averages
print(numpy.mean(data, axis=0))
```

```
[  0.           0.45         1.11666667   1.75         2.43333333   3.15
   3.8          3.88333333   5.23333333   5.51666667   5.95         5.9
   8.35         7.73333333   8.36666667   9.5          9.58333333
  10.63333333  11.56666667  12.35        13.25        11.96666667
  11.03333333  10.16666667  10.           8.66666667   9.15         7.25
   7.33333333   6.58333333   6.06666667   5.95         5.11666667   3.6
   3.3          3.56666667   2.48333333   1.5          1.13333333
   0.56666667]
```

and we can ask what shape the array is

```python
print(numpy.mean(data, axis=0).shape)
```
```
(40,)
```


## 29-Oct-2018 Class notes

* use `def` to define a function within python
