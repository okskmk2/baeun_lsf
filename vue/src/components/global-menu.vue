<template>
  <nav>
    <router-link to="/Profile">
      <span>{{$t('Profile')}}</span>
    </router-link>
    <router-link to="/Portfolio">
      <span>{{$t('Portfolio')}}</span>
    </router-link>
    <router-link to="/Blog">
      <span>{{$t('Blog')}}</span>
    </router-link>
    <router-link to="/Contact">
      <span>{{$t('Contact')}}</span>
    </router-link>
  </nav>
</template>

<i18n>
ko:
  Profile: 프로필
  Portfolio: 포트폴리오
  Blog: 블로그
  Contact: 의뢰하기
en:
  Profile: Profile
  Portfolio: Portfolio
  Blog: Blog
  Contact: Contact
zh:
  Profile: 轮廓
  Portfolio: Portfolio
  Blog: Blog
  Contact: Contact  
</i18n>