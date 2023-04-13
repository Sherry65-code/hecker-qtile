import rwal
import sys

rwal.setwalloc("~/walpap")
rwal.setwalname("walpaper.jpg")
url = rwal.generateURLBySearch("space")
rwal.download(url)
rwal.setwal("--set-zoom-fill")
sys.exit(0)
