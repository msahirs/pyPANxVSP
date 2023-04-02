      integer function locfcn(ia)
! ----------------------------------------------------------------------
      IMPLICIT NONE
      INTEGER ia(*)
!      locfcn  =  POINTER( ia(1) )
  locfcn = LOC(ia(1))
      return
                            ! ==========================================
      END Function Locfcn
