.. _map_classification_ref:

.. currentmodule:: pygeoda

4 Map Classification
====================

pygeoda provids following methods for univariate map classification:

* Hinge box breaks: hinge15_breaks() and hinge30_breaks()
* Natural breaks: natural_breaks()
* Quantile breaks: quantile_breaks()
* Percentile breaks: percentile_breaks()
* Standard deviation breaks: stddev_breaks()

These methods of map classification calculate a corresponding breakpoint 
list for a selected variable.  For more information about the map classification, please read Dr. Luc Anselin's lab note:
http://geodacenter.github.io/workbook/6a_local_auto/lab6a.html. 


4.1 Hinge Box Breaks
--------------------

Hinge Box Breaks calculates a list of breakpoints, including the top, bottom, median, 
and two quartiles of the data. Here the hinge can be 1.5 or 3.0. For example, we can 
call function `hinge15_breaks()` or `hinge30_breaks` with the data "Crm_prp" as input 
parameter:
::

    >>> breaks15 = pygeoda.hinge15_breaks(guerry['Crm_prp'])
    >>> print(breaks15)
    (1190.0, 5990.0, 7624.0, 9190.0, 13990.0)

    >>> breaks30 = pygeoda.hinge30_breaks(guerry['Crm_prp'])
    >>> print(breaks30)
    (-3610.0, 5990.0, 7624.0, 9190.0, 18790.0)


4.2 Natural Breaks
------------------

Natural Breaks calculates a list of breakpoints based on the fracture principle of 
maximum similarity within a group. For example, we can call function `natural_breaks()` 
with the data "Crm_prp" and the number of classification “k” as input parameters:
::

    >>> breaks = pygeoda.natural_breaks(5, guerry['Crm_prp'])
    >>> print(breaks)
    (5521.0, 7204.0, 10237.0, 15890.0)


4.3 Quantile Breaks
-------------------

Quantile Breaks is based on sorted values for a variable that are then grouped 
into bins that each have the same number of observations, the so-called quantiles. 
For example, we can call function  `quantile_breaks()` with the data "Crm_prp", 
and the number of classification “k” as input parameters:
::

    >>> breaks = pygeoda.quantile_breaks(5, guerry['Crm_prp'])
    >>> print(breaks)
    (5439.0, 6886.0, 8205.0, 9584.5)


4.4 Percentile Breaks
---------------------

Percentile Breaks divides the data into six ranges: the lowest 1%, 1-10%, 10-50%, 
50-90%, 90-99% and the top 1%. It returns the range boundaries as a breakpoint list. 
For example, we can call function `natural_breaks()` with the data "Crm_prp" as 
input parameter:
::

    >>> breaks = pygeoda.percentile_breaks(guerry['Crm_prp'])
    >>> print(breaks)
    (1906.3, 4529.0, 7624.0, 10954.0, 19467.8)


4.5 Standard Deviation Breaks
-----------------------------

Standard Deviation Breaks calculates the number of standard deviational units of the 
range from lowest to highest, returning a breakpoint list. For example, we can 
call function `stddev_breaks()` with the data "Crm_prp" as input parameter:
::

    >>> breaks = pygeoda.stddev_breaks(guerry['Crm_prp'])
    >>> print(breaks)
    (1784.1106064421238, 4832.725891456355, 7881.341176470588, 10929.95646148482, 13978.571746499052)

