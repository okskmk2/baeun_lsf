<i18n>
  en: 
    title: Profile
    basic: Basic Information
    education: Education
    workExperience: Work Experience
    phonenumber: +82 1049200523
    address: Seoul, South Korea
    webdeveloper: Web Developer
    moto: Readable site, Best site
    skhynix: SK hynix IT
    hanhwa_onsure: Hanhwa Life Onsure
  ko: 
    title: 프로필
    basic: 기본정보
    education: 교육이수
    workExperience: 실무경험
    phonenumber: 010-4920-0523
    address: 한국 서울시
    webdeveloper: 웹 개발자
    moto: 읽기 쉬운 사이트가 가장 좋은 사이트이다.
    skhynix: SK 하이닉스 정보화
    hanhwa_onsure: 한화생명 온슈어
  ja: 
    title: プロフィール
    phonenumber: +82 1049200523
  zh: 
    title: 轮廓
    phonenumber: +82 1049200523
</i18n>

<template>
  <div>
    <h1>{{ $t('title') }}</h1>
    <section>
      <h2>
        <i class="fa fa-address-card fa-fw mr5"></i>
        {{ $t('basic')}}
      </h2>
      <article>
        <p>
          <i class="fa fa-briefcase fa-fw mr5"></i>
          {{ $t('webdeveloper')}}
        </p>
        <p>
          <i class="fa fa-home fa-fw mr5"></i>
          {{ $t('address')}}
        </p>
        <p>
          <i class="fa fa-envelope fa-fw mr5"></i>
          eunsung.lee@baeun.com
        </p>
        <p>
          <i class="fa fa-phone fa-fw mr5"></i>
          {{ $t('phonenumber')}}
        </p>
        <p>
          <i class="fa fa-comment fa-fw mr5"></i>
          {{ $t('moto')}}
        </p>
      </article>
    </section>
    <section>
      <h2>
        <i class="fa fa-suitcase fa-fw mr5"></i>
        {{ $t('workExperience')}}
      </h2>
      <article>
        <h3>{{ $t('webdeveloper')}} & Server Engineer / {{ $t('skhynix')}}</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2018-01 ~ 2019-07
        </h4>
        <p>IBM LSF 시스템을 파이썬으로 웹, API서버로 확장하였습니다. 개발한 서비스를 국내 2대 서버, 해외 4대 서버를 운영하였습니다.</p>
        <p>기술스택 : Oracle SQL, Mysql, LSF python API, django, Java</p>
        <p>역할 : 설계, 개발, 운영</p>
      </article>
      <article>
        <h3>{{ $t('webdeveloper')}} / {{ $t('hanhwa_onsure')}}</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2017-09 ~ 2017-11
        </h4>
        <p>자바 스프링과 JSP를 사용하여 배치시스템을 개발하고, 해피콜 개발, 카카오링크 연동을 하였습니다. SQL Server를 사용하였습니다.</p>
        <p>기술스택 : SQL Server, Java, Spring MVC</p>
        <p>역할 : 개발</p>
      </article>
      <article>
        <h3>CTO / 아트투게더</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2017-07 ~ 2017-09
        </h4>
        <p>스타트업 초기 기술 로드맵과 자바 스프링을 사용하여 프로토타입의 웹 사이트를 개발하였습니다. MariaDB를 사용하였습니다. 자료 수집을 위해 웹크롤링 작업도 병행하였습니다.</p>
        <p>기술스택 : MariaDB, Java, Spring MVC</p>
        <p>역할 : 프로젝트 설계, 개발, 운영</p>
      </article>
      <article>
        <h3>UI Developer / 농협 IFRS9 구축</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2016-09 ~ 2017-05
        </h4>
        <p>농협 자체 화면 개발도구로 화면을 개발하였고 서버 환경에서 C언어로 회계업무로직을 개발하였습니다. OracleSQL를 사용하였습니다.</p>
        <p>기술스택 : OracleSQL, Jscript(이지빌더), Proframe C</p>
        <p>역할 : 개발</p>
      </article>
      <article>
        <h3>Java Developer / 농협 핀테크 오픈 API 플랫폼 고도화</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2016-04 ~ 2016-09
        </h4>
        <p>자바를 이용하여 핀테크 오픈 API를 개발하였습니다. 신용카드결재API, 제휴기관API를 개발하였습니다.</p>
        <p>기술스택 : Java / JSP</p>
        <p>역할 : 개발</p>
      </article>
    </section>
    <section>
      <h2>
        <i class="fa fa-certificate fa-fw mr5"></i>
        {{ $t('education')}}
      </h2>
      <article>
        <h3>웹기획 고급과정</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2018-12
        </h4>
        <p>기획, 사용자조사, UI/UX기획, 제안서, 견적서 작성법, 프로젝트 관리 실무과정</p>
      </article>
      <article>
        <h3>Angular 5 개발과정</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2018-04
        </h4>
        <p>Angular 5 프론트엔드개발 32시간 수료</p>
      </article>
      <article>
        <h3>한국인터넷 진흥원 핀테크 서비스개발</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2017-07
        </h4>
        <p>핀테크 웹서비스 개발 사례연구 및 프로젝트 리딩</p>
      </article>
      <article>
        <h3>방송통신대학교 컴퓨터과학과</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2016 ~ 2018
        </h4>
        <p>주요 이수과목 : 소프트웨어 공학, 데이터베이스 설계</p>
      </article>
      <article>
        <h3>정보처리산업기사</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2016-04
        </h4>
        <p>주요 내용 : 알고리즘, 데이터베이스 구조, 네트워크 보안</p>
      </article>
      <article>
        <h3>중앙처리컴퓨터학원</h3>
        <h4>
          <i class="fa fa-calendar fa-fw mr5"></i>2015-10 ~ 2016-04
        </h4>
        <p>수석 수료</p>
        <p>주요 이수기술 : OracleSQL, Java, Javascript, Android</p>
      </article>
    </section>
  </div>
</template>
<script>
export default {
  name:'Profile'
}
</script>

<style scoped>
h2 {
  color: #222;
  margin: 0;
}
h3 {
  margin: 1rem 0;
}
h4 {
  margin: 0 0 1rem;
  font-weight: normal;
  color: #555;
}
p{
  line-height: 1.5;
}
section {
  padding: 1rem;
  border-radius: 5px;
  background-color: #fefeff;
  box-shadow: 1px 1px 2px 1px #bbb;
  margin-top: 1rem;
}
article {
  padding: 1rem;
  border-bottom: 1px solid #ddd;
}
</style>
