
from integralstor_utils import command, common
import subprocess


def display(line1, line2=None):
    try:
        bin_path, err = common.get_bin_dir()
        if err:
            raise Exception(err)
        clear()
        if not line1:
            return -1
        if not line2:
            subprocess.Popen(["%s/fpctl" % (bin_path), "move",  '0', '0'])
            subprocess.Popen(["%s/fpctl" % (bin_path), "print",  line1])
        else:
            # print "moving"
            subprocess.Popen(["%s/fpctl" % (bin_path), "move",  '0', '0'])
            # print "printing"
            subprocess.Popen(["%s/fpctl" % (bin_path), "print",  line1])
            # print "moving"
            subprocess.Popen(["%s/fpctl" % (bin_path), "move",  '0', '1'])
            # print "printing"
            subprocess.Popen(["%s/fpctl" % (bin_path), "print",  line2])
    except Exception, e:
        return False, 'Error displaying LCD lines : %s' % str(e)
    else:
        return True, None


def clear():
    try:
        bin_path, err = common.get_bin_dir()
        if err:
            raise Exception(err)
        subprocess.Popen(["%s/fpctl" % (bin_path), "clear"])
    except Exception, e:
        return False, 'Error clearing LCD panel : %s' % str(e)
    else:
        return True, None


def main():

    # display("Line1")
    #display("Disk Errors", "_E_|__|__|__|")
    display("Disk Errorssome", "abcdeabcdeabcdea")
    # clear()


if __name__ == "__main__":
    main()

# vim: tabstop=8 softtabstop=0 expandtab ai shiftwidth=4 smarttab
