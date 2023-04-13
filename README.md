# Hecker Qtile

- This is my custom configuration for qtile

- Save autostart.sh to $HOME

    ```bash
    cp ./autostart.sh /home/$(whoami)/
    ```

- Copy qtile directory to $HOME/.config

    ```bash
    cp -r ./qtile /home/$(whoami)/.config/
    ```

- Install these packages

    ```bash
    sudo pacman -Sy qtile dmenu nitrogen xcompmgr
    ```

- Display set Python program for those who have a laptop but only want to use their secondary monitor

    ```bash
    cp ./.displayset.py /home/$(whoami)/
    ```

*This script will not do anything to those using a single monitor or laptop.*

**ENJOY 😃**
