# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
#########################################################################

def index():
    
    return locals()

def add_daily():
    return locals()
def addmanage():
    return locals()

def addoct():
    form=SQLFORM(db.doct).process()
    if form.accepted:
        session.flash = 'تم اضافة اسم الطبيب بنجاح'
    elif form.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    rows=db(db.doct).select()
    return dict(form=form,rows=rows)

def edit_doct():
    id=request.args(0,cast=int) or redirect(URL('index'))
    form=SQLFORM(db.doct,id,deletable = True).process(next='view_manage/[id]')
    if form.accepted:
        session.flash = 'تم تعديل الطلب بنجاح'
    elif form.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    return locals()


def addprod():
    form=SQLFORM(db.prod).process(next='view_manage/[id]')
    if form.accepted:
        session.flash = 'تم اضافة نوع الفحص بنجاح'
    elif form.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    rows=db(db.prod).select()
    return locals()

def edit_prod():
    id=request.args(0,cast=int) or redirect(URL('index'))
    form=SQLFORM(db.prod,id,deletable = True).process()
    if form.accepted:
        session.flash = 'تم تعديل الطلب بنجاح'
    elif form.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    return locals()


def add_orday():
    form=SQLFORM(db.orday).process(next='view_order/[id]')
    if form.accepted:
        session.flash = 'تم اضافة الطلب بنجاح'
    elif form.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    return locals()

def view_order():
    id=request.args(0,cast=int) or redirect(URL('index'))
    rows=db(db.orday.id==id).select()
    return locals()

def edit_order():
    id=request.args(0,cast=int) or redirect(URL('index'))
    form=SQLFORM(db.orday,id,deletable = True).process(next='view_order/[id]')
    if form.accepted:
        session.flash = 'تم تعديل الطلب بنجاح'
    elif form.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    return locals()


def add_expe():
    form=SQLFORM(db.expe).process()
    if form.accepted:
        session.flash = 'تم اضافة المصروفات بنجاح'
    elif form.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    return locals()



def edit_expe():
    id=request.args(0,cast=int) or redirect(URL('index'))
    forms=SQLFORM(db.expe,id,deletable = True).process()
    if forms.accepted:
        session.flash = 'تم تم تعديل المنصرف بنجاح'
    elif forms.errors:
        response.flash = 'هناك خطأ'
    else:
        response.flash = 'من فضلك استكمل البيانات'
    return locals()



def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
