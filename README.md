# Capture One Keyword Renamer

An inconvenient flaw of [Capture One](https://www.captureone.com/) is the lack of capability to export keywords into file names.
Users have been complaining this for years [[1]](https://support.captureone.com/hc/en-us/community/posts/360012246777-Export-Naming-Token-for-Keywords-)[[2]](https://support.captureone.com/hc/en-us/community/posts/360015617817-key-words-and-export)[[3]](https://support.captureone.com/hc/en-us/community/posts/360009400578-How-to-export-a-image-naming-as-the-keyword) but it seems Capture One has no plans to work on this. So I develop this simple script. The idea is we can first export the JPG files, and then use this script to extract the store keywords in the IPTC tags so we could rename the files.

## Usage

This is a python script, which requires a python environment and some knowledge on command lines and how python works.
After first cloning the repo, use `python -m pip install -r requirements` to install the dependencies.

How to use the script:

First, ensure you have the keywords exported into the JPG files.
This could be done by going to "Export Images," tick the "Show all options," and change the Keywords drop down menu in the Metadata tab to "All."

![Screenshot of how to have keywords exported.](https://github.com/grapeot/CaptureOneKeywordsRenamer/blob/master/export.jpg?raw=true)

Second, copy the script into the folder you wish to rename the images.
Run `python CaptureOneRenamer.py` in the folder.
The script will read the IPTC tags, get new file names, and **copy** the files to new names.
After confirming everything looks correct, you can then manually delete the old images.

If there are interests on this project, I may also release it as an exe file.
