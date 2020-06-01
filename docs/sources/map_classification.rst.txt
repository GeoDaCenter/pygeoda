.. _map_classification_ref:

.. currentmodule:: pygeoda

8 Map Classification
================================

pygeoda 0.0.4 provids following methods for univariate
map classification:

* Hinge box breaks: hinge15_breaks() and hinge30_breaks()
* Natural breaks: natural_breaks()
* Quantile breaks: quantile_breaks()
* Percentile breaks: percentile_breaks()
* Standard deviation breaks: stddev_breaks()

In the pygeoda v0.0.4, the methods of map classification calculate a corresponding breakpoint 
list of the variables. Hree we will only introduce how to call thesemethods using pygeoda. 
For more information about the map classification, please read the lab note that Dr. Luc Anselin wrote:
http://geodacenter.github.io/workbook/6a_local_auto/lab6a.html. 


8.1 Hinge Box Breaks
---------------

Hinge15 breaks calculate a list of breakpoints, including the top, bottom, median, 
and two quartiles of the data. Here the hinge can be 1.5 or 3.0. For example, we can 
call function `hinge15_breaks()` or `hinge30_breaks` with the data “crm_prp” as input 
parameter:
::

    >>> breaks15 = pygeoda.hinge15_breaks(crm_prp)
    >>> breaks30 = pygeoda.hinge30_breaks(crm_prp)


8.2 Natural Breaks
---------------

Natural breaks Calculate of a breakpoint list based on the fracture principle of 
maximum similarity within a group. For example, we can call function `natural_breaks()` 
with the data “crm_prp” and the number of classification “k” as input parameters:
::

    >>> breaks = pygeoda.natural_breaks(k, crm_prp)

8.3 Quantile Breaks
---------------

The quantile breaks is based on sorted values for a variable that are then grouped 
into bins that each have the same number of observations, the so-called quantiles. 
Here the number of quantiles is variable. For example, we can call function 
`quantile_breaks()` with the data “crm_prp” the number of classification “k” as input
parameter:
::

    >>> breaks = pygeoda.quantile_breaks(k, crm_prp)

8.4 Percentile Breaks
---------------

The percentile breaks divides the data to  six ranges, the lowest 1%, 1-10%, 10-50%, 
50-90%, 90-99% and the top 1%, returning the range boundaries as a breakpoint list. 
. For example, we can call function `natural_breaks()` with the data “crm_prp” as 
input parameter:
::

    >>> breaks = pygeoda.percentile_breaks(crm_prp)

8.5 Standard Deviation Breaks
---------------

Standard deviation breaks calculate the number of standard deviational units of  the 
range from lowest to highest, returning a breakpoint list. . For example, we can 
call function `stddev_breaks()` with the data “crm_prp” as input parameter:
::

    >>> breaks = pygeoda.stddev_breaks(crm_prp)
