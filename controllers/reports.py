# -*- coding: utf-8 -*-
# try something like
def index():
    return locals()

    
    
    
def orders():
    form=SQLFORM.factory(Field('startd','date',requires=IS_NOT_EMPTY(),label='من يوم'),
                         Field('endd','date',label='إلى يوم'))
    if form.process().accepted:
        response.flash = 'تم عرض المده المحددة'
        st=form.vars.startd
        en=form.vars.endd or form.vars.startd
        days=(db.orday.ordate>=st)&(db.orday.ordate<=en)
    else:
        response.flash = 'منفضلك اختار مده محددة'
        days=(db.orday)
    page=request.args(0,cast=int,default=0)
    sta=page*10
    end=sta+10
    rows=db(days).select(limitby=(sta,end))
    todaysum=db(days).select(db.orday.totalcost.sum())
    count=db(days).select(db.orday.totalcost.count())
    return locals()


    
def doc_report():
    form=SQLFORM.factory(Field('doct','referenc doct',requires=IS_IN_DB(db,db.doct.id,'%(docname)s'),label='اختار اسم الدكتور'),
                        Field('startd','date',requires=IS_NOT_EMPTY(),label='من يوم'),
                        Field('endd','date',label='إلى يوم'))
    if form.process().accepted:
        id=form.vars.doct
        st=form.vars.startd
        en=form.vars.endd or form.vars.startd
        docq=(db.orday.docname==id)&(db.orday.ordate>=st)&(db.orday.ordate<=en)
    else:
        docq=(db.orday.docname==1)
    page=request.args(0,cast=int,default=0)
    sta=page*10
    end=sta+10    
    rows=db(docq).select(limitby=(sta,end))
    todaysum=db(docq).select(db.orday.totalcost.sum())
    count=db(docq).select(db.orday.totalcost.count())

    return locals()


def view_expe():
    form=SQLFORM.factory(Field('startd','date',requires=IS_NOT_EMPTY(),label='من يوم'),
                         Field('endd','date',label='إلى يوم'))
    if form.process().accepted:
        response.flash = 'تم عرض المده المحددة'
        st=form.vars.startd
        en=form.vars.endd or form.vars.startd
        days=(db.expe.expedate>=st)&(db.expe.expedate<=en)
    else:
        response.flash = 'منفضلك اختار مده محددة'
        days=(db.expe)
    page=request.args(0,cast=int,default=0)
    sta=page*10
    end=sta+10
    rows=db(days).select(limitby=(sta,end))
    todaysum=db(days).select(db.orday.totalcost.sum())
    count=db(days).select(db.expe.expemount.count())
    
    return locals()
