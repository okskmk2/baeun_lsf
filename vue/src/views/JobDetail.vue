<i18n>
en:
    title: Job
    Requeue: Requeue
    Kill: Kill
    Top: Top
ko:
    title: 잡
    Requeue: Requeue
    Kill: Kill
    Top: Top
</i18n>

<template>
    <div>
        <div class="row jc-between" style="margin-bottom: 12px">
        <h1>{{ $t('title') }} : {{ $route.params['jobId'] }} <span class="status-text">{{jobStatus}}</span></h1>
            <div>
                <button style="margin-right: 5px">{{$t('Requeue')}}</button>
                <button style="margin-right: 5px">{{$t('Kill')}}</button>
                <button>{{$t('Top')}}</button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'JobDetail',
        data(){
            return {
                jobStatus:'Run'
            }
        }
    }
</script>