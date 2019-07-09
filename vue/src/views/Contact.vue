<i18n>
  en: 
    title: Request
    q1: Which platform do you want?
    q2: What is the purpose?
    q3: Which stage you do in?
    q4: When is due date?
    q5: Please write your email.
    web: Web
    android_mobile: Android
    linux: Linux
    idea_stage: Only has Idea.
    IA_stage: Web Menu defined.
    UI_stage: UI defined.
    Next: Next
    Previous: Previous
  ko: 
    title: 의뢰하기
    q1: 어떤 플랫폼을 원하세요?
    q2: 용도가 뭔가요?
    q3: 어디까지 기획하였나요?
    q4: 언제까지 개발해야하나요?
    q5: 응답받으실 이메일을 적어주세요.
    web: 웹
    android_mobile: 안드로이드
    linux: 리눅스
    idea_stage: 아이디어만 있다.
    IA_stage: 웹 메뉴까지 정의했다.
    UI_stage: 화면까지 구상했다.
    Next: 다음
    Previous: 이전
</i18n>

<template>
  <div>
    <h1>{{ $t('title') }}</h1>
    <section>
      <div class="stepper">
        <span class="tag">1</span>
        <span class="tag">2</span>
        <span class="tag">3</span>
      </div>
      <article>
        <div class="question">{{ $t('q1') }}</div>
        <div class="answer">
          <label for="web">
            {{ $t('web') }}
            <input type="checkbox" id="web" />
          </label>
          <br />
          <label for="android_mobile">
            {{ $t('android_mobile') }}
            <input type="checkbox" id="android_mobile" />
          </label>
          <br />
          <label for="linux">
            {{ $t('linux') }}
            <input type="checkbox" id="linux" />
          </label>
        </div>
        <div class="question">{{ $t('q2') }}</div>
        <div class="answer">
          <input type="text" maxlength="300" class="a2" />
        </div>
      </article>
      <article>
        <div class="question">{{ $t('q3') }}</div>
        <div class="answer">
          <div class="rel">
            <hr />
            <div class="pointer-box">
              <div class="pointer">
                <input type="radio" name="stage" id="idea_stage" />
                <div>&#9660;</div>
                <label for="idea_stage">{{ $t('idea_stage') }}</label>
              </div>
              <div class="pointer">
                <input type="radio" name="stage" id="IA_stage" />
                <div>&#9660;</div>
                <label for="IA_stage">{{ $t('IA_stage') }}</label>
              </div>
              <div class="pointer">
                <input type="radio" name="stage" id="UI_stage" />
                <div>&#9660;</div>
                <label for="UI_stage">{{ $t('UI_stage') }}</label>
              </div>
            </div>
          </div>
        </div>
        <div class="question">{{ $t('q4') }}</div>
        <div class="answer">
          <input type="date" />
        </div>
      </article>
      <article>
        <div class="question">{{ $t('q5') }}</div>
        <div class="answer">
          <input type="email">
        </div>
      </article>
      <div class="row jc-between">
        <button>{{ $t('Previous') }}</button>
        <button>{{ $t('Next') }}</button>
      </div>
    </section>
  </div>
</template>
<style lang="less" scoped>
hr {
  position: absolute;
  width: 100%;
  top: 7px;
}
.pointer-box {
  display: flex;
}
.pointer {
  text-align: center;
  flex-grow: 1;
  z-index: 2;
  input {
    display: none;
  }
  input:checked + div {
    color: red;
  }
}
section {
  padding: 3rem;
  border-radius: 5px;
  background-color: #fefeff;
  box-shadow: 1px 1px 2px 1px #bbb;
  margin-top: 2rem;
}
.question {
  font-size: 1.5rem;
}
.answer {
  margin: 1rem 1rem 2rem;
  line-height: 2;
}
.a2 {
  margin-top: 2rem;
  display: block;
  width: 100%;
  box-sizing: border-box;
  padding: 1rem;
}

button {
  font-size: 20px;
  padding: 4px 12px;
  color: #333;
}

.stepper {
  display: flex;
  justify-content: space-around;
  margin-bottom: 2rem;
}

.tag {
  width: 40px;
  height: 40px;
  border-radius: 40px;
  background-color: #0089f4;
  color: white;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
}

@media screen and (max-width: 650px) {
  section {
    padding: 1rem;
  }
}
</style>

