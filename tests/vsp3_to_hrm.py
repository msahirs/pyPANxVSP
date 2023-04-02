from __future__ import print_function

import openvsp as vsp
import time


def test_func():
    vsp.ReadVSPFile("test_vsp.vsp3")

    vsp.ExportFile( "text_hrm.hrm", vsp.SET_ALL, vsp.EXPORT_XSEC)

    vsp.VSPRenew()

# Check for errors

def main():

    stdout = vsp.cvar.cstdout
    errorMgr = vsp.ErrorMgrSingleton.getInstance()

    iterations = 1

    start = time.time() # start of wall time

    for i in range(iterations): test_func()

    end = time.time() # end of wall time

    print(f"\nTotal execution time for {iterations} loops = {(end-start):.8} seconds ",)
    # print(f"\nTime spent per loop = {(end-start) * 10e3 /(iterations):.8} milliseconds ",)

    # Error collection #

    num_err = errorMgr.GetNumTotalErrors()
    for i in range(0, num_err):
        err = errorMgr.PopLastError()
        print("error = ", err.m_ErrorString)

if __name__ == "__main__":
    main()