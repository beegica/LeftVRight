from smile.common import *
from config import pres_dur, pres_isi, pres_jitter, instructions
from listgen import genStim


blocks = genStim()


exp = Experiment()

Wait(1.)
RstDocument(text=instructions, height=exp.screen.height,
            width=.6*exp.screen.width)
with UntilDone():
    KeyPress()
Wait(1.)
with Loop(blocks) as block:
    Wait(1.)
    with Parallel():
        Label(text="New Block Starting, press any key!")
        Pulse()
    with UntilDone():
        KeyPress()

    with Loop(block) as trial:
        fix = Label(text="+", font_size=pres_font_size)
        with UntilDone():
            Wait(.5)

            with If(trial.current['stim'] == "left"):
                Label(text="<",
                      right=fix.left,
                      duration=pres_prep,
                      font_size=pres_font_size)
            with Else():
                Label(text=">",
                      left=fix.right,
                      duratio=pres_prep,
                      font_size=pres_font_size)

            Wait(.5)

            with If(trial.current['stim'] == "left"):
                Label(text="<",
                      right=fix.left,
                      duration=pres_dur,
                      font_size=pres_font_size)
            with Else():
                Label(text=">",
                      left=fix.right,
                      duratio=pres_dur,
                      font_size=pres_font_size)

            Wait(pres_isi, jitter=pres_jitter)

exp.run()
