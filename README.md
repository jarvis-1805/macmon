# macmon

macmon is a simple tool to get and change MAC address and mode of any adapter in linux.

## How to install

```bash
#!/bin/bash
git clone https://github.com/jarvis-1805/macmon.git
cd macmon
sudo ./macmon.sh
```

## File permisions

Before executing ```macmon.sh``` provide relevant permissions:

```bash
#!/bin/bash
chmod +x macmon.sh
```

## Usage (Commands)

* To get MAC Address

```bash
#!/bin/bash
> macmon --interface [interface name] --getMAC
```

* To change MAC Address

```bash
#!/bin/bash
> macmon --interface [interface name] --changeMAC [new MAC]
```

* To get MODE

```bash
#!/bin/bash
> macmon --interface [interface name] --getMODE
```

* To change MODE

```bash
#!/bin/bash
> macmon --interface [interface name] --changeMODE [new MODE]
```

* To EXIT

```bash
#!/bin/bash
> macmon exit
```

Note: Commands can also be given simultaneously:

* To get and change MAC Address

```bash
#!/bin/bash
> macmon --interface [interface name] --getMAC --changeMAC [new MAC]
```

* To get and change MODE

```bash
#!/bin/bash
> macmon --interface [interface name] --getMODE --changeMODE [new MODE]
```

##### _P.S. Shortcut arguments can always be given..._
