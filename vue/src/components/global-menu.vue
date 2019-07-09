<template>
    <nav>
        <router-link to="/Jobs">
            <span>{{$t('Jobs')}}</span>
        </router-link>
        <router-link to="/Queues">
            <span>{{$t('Queues')}}</span>
        </router-link>
        <router-link to="/Hosts">
            <span>{{$t('Hosts')}}</span>
        </router-link>
        <router-link to="/Users">
            <span>{{$t('Users')}}</span>
        </router-link>
        <hr>
        <router-link to="/Config">
            <span>{{$t('Config')}}</span>
        </router-link>
        <router-link to="/Limits">
            <span>{{$t('Limits')}}</span>
        </router-link>
        <router-link to="/Logs">
            <span>{{$t('Logs')}}</span>
        </router-link>
    </nav>
</template>

<i18n>
ko:
    Jobs: 잡
    Queues: 큐
    Hosts: 호스트
    Users: 사용자
    Config: 환경설정
    Limits: 한계설정
    Logs: 로그
en:
    Jobs: Jobs
    Queues: Queues
    Hosts: Hosts
    Users: Users
    Config: Config
    Limits: Limits
    Logs: Logs
</i18n>