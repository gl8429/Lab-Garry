#!/usr/bin/python

import sys

import os

import re

from subprocess import Popen, PIPE



def git_filesize_hook(chars_cutoff=80, verbose=False):

    cmd = "git ls-tree --name-only --full-tree -r -l HEAD"

    StagesFiles = Popen(cmd, shell=True, stdout=PIPE, cwd=os.getcwd())

    for StagedFile in  StagesFiles.stdout.readlines():

        chars=0

        if verbose: print StagedFile

        with open(os.getcwd()+'/' + StagedFile.split("\n")[0]) as f:

          for line in f:

            chars=len(line)

            if chars>80:

              print os.getcwd()+'/' + StagedFile.split("\n")[0] +" has a line of "+str(chars) +" characters!"

              return ("Your Commits contains at least one file has a line with more than %d characters" % chars_cutoff )

    return 0



if __name__ == "__main__":

    sys.exit(git_filesize_hook(80, False))