import datetime

db.define_table('doct',
                Field('docname','string',requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'doct.docname')],label='دكتور الاشعة'),
               Field('mobile',label='رقم الموبيل'),Field('address',label='العنوان'))

db.define_table('prod',
                Field('prodname','string',label='الفحص',requires=[IS_NOT_EMPTY(),IS_NOT_IN_DB(db,'prod.prodname')]),
               Field('prodcost','integer',label='تكلفة الفحص',requires=IS_NOT_EMPTY()))

db.define_table('orday',
                Field('custname','string',requires=IS_NOT_EMPTY(),label='اسم العميل'),
                Field('docch','string',requires=IS_NOT_EMPTY(),label='طبيب الكشف'),
                Field('docname','reference doct',requires=IS_IN_DB(db,db.doct.id,'%(docname)s'),label='دكتور الاشعة'),
                Field('prodname','reference prod',requires=IS_IN_DB(db,db.prod.id,'%(prodname)s'),label='نوع الفحص'),
                Field('sabgha','integer',default=0,label='سعر الصبغه'),
                Field('totalcost',compute=lambda row: db.prod(row['prodname']).prodcost+row['sabgha'],label='إجمالى المبلغ'),
                Field('ordate','date',default=request.now,label='تاريخ اليوم'),
                Field('ortime','datetime',default=request.now,writable=False,label='الوقت'),
                Field('notes','text',label='ملاحظات'))


db.define_table('expety',Field('expetype'))
db.define_table('expe',
               Field('expename',label='اسم المصروفات'),
               Field('expemount','integer',default=0,label='قيمة المبلغ'),
               Field('expedate','date',default=datetime.date.today,label='تاريخ الصرف'),
               Field('expetype','reference expety',default=1,requires=IS_IN_DB(db,db.expety.id,'%(expetype)s'),label='نوع المصروفات'))

db.define_table('treasury',
               Field('tr_name',requires=IS_NOT_EMPTY(),label='بيان'),
               Field('tr_input','integer',default=0,label='توريد'),
               Field('tr_output','integer',default=0,label='مسحوبات'),
               Field('tr_date','date',default=request.now,))
