// _mock.js
// ��Ӧ��rurl�ᱻ�м�����أ�������mock����
//�����ʵ�����Կ�http://mockjs.com/examples.html#Number
// ANY localhost:9999/
Mock.mock('/', {
    data: [],
    msg: "hello mock",
    "code|1-4": 1,
})

// ��¼mp
Mock.mock('/mp/v1_0/authorizations', 'POST', {
    message: "OK",
    data: {
      token: "eyJ0eXAi",
      refresh_token: "eyJ0eXAi",
      id: "19933333333",
      name: "19933333333",
      photo: "https://github.githubassets.com/images/modules/dashboard/onboarding/gh-desktop.png"
    }
})

// ��������mp
Mock.mock('/mp/v1_0/articles', 'POST', {
  message: "OK",
  data: {
    id: 123
  }
})

// ��¼mis
Mock.mock('/mis/v1_0/authorizations', 'POST', {
  message: "OK",
  data: {
    token: "eyJ0eXAi"
  }
})

// ��ѯ����mis
Mock.mock('/mis/v1_0/articles', 'GET', {
message: "OK",
data: {
  articles:[{
    article_id: 123,
    title: "x"
  }]
}
})

// �������mis
Mock.mock('/mis/v1_0/articles', 'PUT', {
  message: "OK"
  })

// ��¼app
Mock.mock('/app/v1_0/authorizations', 'POST', {
  message: "OK",
  data: {
    token: "eyJ0eXAi"
  }
})

// ��ѯƵ������app
Mock.mock('/app/v1_0/articles', 'GET', {
message: "OK",
data: {
  results:[{
    article_id: 123,
    title: "x"
  }]
}
})



// ��չrtype��֧��jsonp��ʽ��ʹ��param�����Ӧ�Ļص���
// GET JSONP localhost:9999/test
Mock.mock('/test', {
    type: 'jsonp',
    param: 'callbackName'
},{
    code: 0,
    msg: 'hello from mock jsonp',
    data: {
        "id|1000-9999": 1,
    }
})

// Ĭ�ϻص����� callback
Mock.mock("/test2", "jsonp", {
    code: 0,
    msg: "hello from mock jsonp2",
    data: {
        "id|1000-9999": 1,
    }
});

// Ĭ�ϻص����� callback
Mock.mock("/test3", "jsonp", {
    code: 0,
    msg: "hello from mock jsonp2",
    data: {
        "object|2": {
	"310000": "�Ϻ���",
    	"320000": "����ʡ",
   	 "330000": "�㽭ʡ",
    	"340000": "����ʡ"
          },
    }
});

// Ĭ�ϻص����� callback
Mock.mock("/test4", "jsonp", {
  code: 0,
  msg: "hello from mock jsonp2",
  data: {
      "object|2": {
"310000": "�Ϻ���",
    "320000": "����ʡ",
    "330000": "�㽭ʡ",
    "340000": "����ʡ"
        },
  }
});