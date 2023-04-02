from __future__ import print_function

import openvsp as vsp
import time


def test_func():
    vsp.ReadVSPFile("ss2_fix.vsp3")

    vsp.ExportFile( "text_hrm.hrm", vsp.SET_ALL, vsp.EXPORT_XSEC)

    start = time.time()
    vsp.VSPRenew()
    end = time.time()

    return end-start

# Check for errors

def main():

    stdout = vsp.cvar.cstdout
    errorMgr = vsp.ErrorMgrSingleton.getInstance()

    iterations = 20
    renew_time = 0

    start = time.time() # start of wall time

    for i in range(iterations):
        renew_time += test_func()

    end = time.time() # end of wall time

    print(f"\nTotal execution time for {iterations} calls = {(end-start):.5} seconds ",)
    print(f"\n Avg time spent per call = {(end-start) /(iterations):.5} seconds ",)
    print(f"\n Avg time spent renewing per call = {(renew_time) /(iterations):.5} seconds ",)

    # Error collection #

    num_err = errorMgr.GetNumTotalErrors()
    for i in range(0, num_err):
        err = errorMgr.PopLastError()
        print("error = ", err.m_ErrorString)

if __name__ == "__main__":
    main()