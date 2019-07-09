<i18n>
  en: 
    title: Queues
  ko: 
    title: 큐
</i18n>

<template>
  <div>
    <h1>{{ $t('title') }}</h1>
    <hot-table :settings="settings" licenseKey="non-commercial-and-evaluation"></hot-table>
  </div>
</template>

<script>
    import {HotTable} from '@handsontable/vue';

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
        }
    }
</script>