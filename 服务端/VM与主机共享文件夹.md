# VM与主机共享文件夹

```bash
mkdir /mnt/hgfs
mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs -o allow_other
```
