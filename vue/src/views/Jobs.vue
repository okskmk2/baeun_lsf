<i18n>
en:
    title: Jobs
    Download: Download
    Settings: Settings
ko:
    title: 잡
    Download: 다운로드
    Settings: 설정
</i18n>

<template>
    <div>
        <h1>{{ $t('title') }}</h1>
        <div class="row jc-between" style="margin-bottom: 12px">
            <div class="row-in">
                <input type="search" style="margin-right: 5px">
                <button><i class="material-icons">search</i></button>
            </div>
            <div>
                <button style="margin-right: 5px">{{$t('Download')}}</button>
                <button>{{$t('Settings')}}</button>
            </div>
        </div>
        <hot-table :settings="settings" licenseKey="non-commercial-and-evaluation" ref="hot"></hot-table>
    </div>
</template>

<script>
    import {HotTable} from '@handsontable/vue';
    import Handsontable from 'handsontable';

    export default {
        name: 'Jobs',
        data() {
            return {
                settings: {
                    data: [
                        [1, 'Test1', 'hoho', 'default', 'normal', 'Pend', 'Submit Host : s032x', 'Submit Date : 2019-02-01', 'Pend time : 3s'],
                        [2, 'Test2', 'jojo', 'default', 'normal', 'Run', 'Ex Host : v056c', 'Start Date : 2019-02-01', 'Run time : 7h 4m 2s'],
                        [3, 'Test3', 'bobo', 'default', 'normal', 'Pend', 'Submit Host : s032x', 'Submit Date : 2019-02-01', 'Pend time : 3s'],
                        [4, 'Test4', 'jojo', 'default', 'normal', 'Pend', 'Submit Host : s032x', 'Submit Date : 2019-02-01', 'Pend time : 3s'],
                    ],
                    rowHeaders: true,
                    colHeaders: [
                        'ID', 'Name', 'User', 'Project', 'Queue', 'Status', 'Host', 'Date', 'Time'
                    ],
                    stretchH: 'all',
                    licenseKey: 'non-commercial-and-evaluation'
                }
            };
        },
        components: {
            HotTable
        },
        mounted(){
            Handsontable.hooks.add('beforeOnCellMouseDown', (evt, coords)=>{
                if( coords.row !== -1){
                    if (coords.col === 0){
                        let jobId = this.$refs.hot['hotInstance'].getDataAtCell(coords.row, coords.col);
                        this.$router.push({ name: 'JobDetail', params: { jobId: jobId }})
                    }
                }
            }, this.$refs.hot['hotInstance']);
        }
    }
</script>