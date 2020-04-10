# oscplotlib

Use Matplotlib in terminals that support the OSC 1337 image protocol.

Example:

    import matplotlib.pyplot as plt
    import oscplotlib as osc

    plt.plot([1, 2, 3])
    osc.show()

    plt.figure(2)
    plt.plot([3, 2, 1])

    plt.figure(3)
    plt.hist([1, 1, 2])

    osc.show_all()

