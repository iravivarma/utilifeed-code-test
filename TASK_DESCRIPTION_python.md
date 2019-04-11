# TASK
* Write a Python program which reads timeseries data from fluid streams (for example pipes with hot water running through them) and calculates their _aggregate stream_, which represents the stream that would result if we physically combined all input streams.
*   The streams individually are defined by temperature and flow. For the aggregate stream you need to calculate the aggregated flow and flow-weighted temperature.
* Use the provided sample data to create a set of tests for testing the critical parts of your application.
*   It's up to you to decide exactly which aspects should be encapsulated by unit tests. Write tests of a style you actually would write for a CI/CD suite.
* While the program is running, it listen for .csv files being added/removed to the ./input folder. Whenever the contents of the folder changes, it re-calculates the aggregate stream and saves it to ./output/stream_aggregate.csv.

## Mathematical definitions
* Flow-weighted temperature is a weighted average temperature, where the impact of each stream on the "average" is proportional to the streams flow at that time.
* The values in the aggregate stream is calculated independently for each timestamp
Stream i has, at each timestamp t, a flow `f_i(t)` and a temperature `T_i(t)`
Aggregated flow (`f`) is calculated as a simple sum each hour. For `n` streams:
    `f(t) = (f_0(t) + f_1(t) + ... + f_n(t) )`
Flow-weighted temperature `T_fw(t)` is calculated as:
    `T_fw(t) = (T_0(t)*f_0(t) + T_1(t)*f_1(t) + ... + T_n(t)*f_n(t)) / (f_0(t) + f_1(t) + ... + f_n(t)) = (T_0(t)*f_0(t) + T_1(t)*f_1(t) + ... + T_n(t)*f_n(t)) / f(t)`

## Sample data
* 3 streams with 24 hours of hourly data is provided
* Each dataset has 3 columns: datetime, flow, temperature
* The aggregated stream should have the exact same column names and formats as input streams
* The data in the output file should have the same resolution as the input files (2 figures to the right of the decimal point)

## Tools
* We don't require any specific set of libraries of frameworks to solve this task, use what you believe to be an efficient choice to perform the task.

## To Deliver
* Source code for a program which:
*   Reads indata from ./input (one file per stream, called 'stream_i.csv') 
*   Saves results to ./output/stream_aggregate.csv (same column names as input streams)
*   Contains (passing) unit tests that encapsulate the critical pieces of the program

## Scope
* We expect that even if some aspects of the task are new to the participant, time to complete should not have to exceed a few hours.
*   For reference, a python script that performs the aggregation can be written in a few minutes, so most of the time will probably be spent on IO and writing tests.
*   Production-grade stability features like watchdogs, inter-session storage etc are not expected to be implemented, but feel free to add comments about where and how you would implement them if this was a "real" application.
*   Your code does not need to handle edge cases, and your test suite is not expected to be all-encompassing. However, please specify in code comments which edge cases you do or do not take into account.

* In a production application, there are many edge-case considerations you'd have to take care of, like missing data, divide-by-0 errors, datasets larger than memory etc.
* To keep this excercise relatively short, you are not required to take care of any such cases which do not show up in our sample files.
* You may assume that:
*   There are no rows with combined 0 flow
*   There are no rows with missing data
*   All datastreams have the same datetime vector
* Your program should be able to handle:
*   A variable number of streams (but don't worry about physical memory limit)
*   Variable lengths of the streams (assuming all streams have the same length)

## Contact
Questions, clarifications and uncertainties, email:
jens@utilifeed.com
