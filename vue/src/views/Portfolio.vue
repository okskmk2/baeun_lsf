<i18n>
  en: 
    title: Portfolio
  ko: 
    title: 포트폴리오
  ja: 
    title: こんにちは、世界！
  zh: 
    title: 你好、世界！
</i18n>

<template>
  <div>
    <h1>{{ $t('title') }}</h1>
    <article>
      <h2>fbank</h2>
      <p>은행, IFRS9</p>
      <p>jsp</p>
    </article>
    <article>
      <h2>건물 관리자</h2>
      <p>건물관리 웹사이트</p>
      <p>vue, django</p>
    </article>
    <article>
      <h2>민원24</h2>
      <p>민원청구</p>
      <p>전사정부프레임워크</p>
    </article>
    <article>
      <h2>부하분산시설</h2>
      <p>대규모 작업을 처리하기 위한 부하분산 시스템</p>
      <p>jsp</p>
    </article>
    <article>
      <h2>식당</h2>
      <p>각종 메뉴 소개, 찾아오늘 길</p>
      <p>윅스</p>
    </article>
    <article>
      <h2>마켓</h2>
      <p>누구나 상품을 올릴 수 있다.</p>
      <p>고도몰</p>
    </article>
    <article>
      <h2>사회문제연구소</h2>
      <p>정책제안</p>
      <p>vue, express</p>
    </article>
    <article>
      <h2>PMS</h2>
      <p>프로젝트 관리</p>
      <p>django</p>
    </article>
  </div>
</template>
<style scoped>
h2 {
  margin: 1rem;
}
article {
  padding: 2rem;
  display: inline-block;
  width: 510px;
  border: 1px solid #ddd;
  height: 20rem;
  margin: 0 1rem 1rem 0;
}
@media screen and (max-width: 650px) {
  article {
    padding: 1rem;
    width: auto;
    display: block;
    margin: 1rem 0;
  }
}
</style>

