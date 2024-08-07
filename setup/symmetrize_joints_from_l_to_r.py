# -*- coding: utf-8 -*-
# 骨左右対称化

import maya.cmds as cmds
import cymel.main as cm


# 選択以下の骨を取得
joints = cm.Os(cmds.ls(sl=True, dag=True, type="joint"))

# 左側の骨を取得
lefts = []
for i in joints:
    if str(i).startswith("L"):
        lefts.append(i)


#=========================================
# 骨の値をまとめて、丸める
#=========================================
for i in joints:
    node = cm.O(i)
    
    transform = [node.tx.get(), node.ty.get(), node.tz.get(), 
                 node.rx.get(), node.ry.get(), node.rz.get(), 
                 node.sx.get(), node.sy.get(), node.sz.get()]
    
    # 値を小数点第三位までに丸める
    transform = [round(num, 3) for num in transform]
    
    i.t.set((transform[0], transform[1], transform[2]))
    i.r.set((transform[3], transform[4], transform[5]))
    i.s.set((transform[6], transform[7], transform[8]))


#=========================================
# L→Rに値コピー
#=========================================
for left in lefts:
    right = cm.O(str(left).replace("L", "R"))
    
    left.tx.set(-right.tx.get())
    left.ty.set(right.ty.get())
    left.tz.set(right.tz.get())
    left.rx.set(right.rx.get())
    left.ry.set(right.ry.get())
    left.rz.set(right.rz.get())
    left.sx.set(right.sz.get())
    left.sy.set(right.sy.get())
    left.sz.set(right.sz.get())
