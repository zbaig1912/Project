<template>
    <div id="app">
        <TabNav :tabs="['USERS', 'TRANSACTIONS']" :selected="selected" @selected="setSelected" >
            <Tab :isSelected="selected === 'USERS'">
                <Table :headers="['ID', 'Name', 'Email', 'Firm']" :tabSelected=selected></Table>
            </Tab>
            <Tab :isSelected="selected === 'TRANSACTIONS'" >
                <Table :headers="['ID', 'Product', 'Total', 'User']" :tabSelected=selected></Table>
            </Tab>
        </TabNav>
    </div>
</template>

<script>
    import TabNav from './components/TabNav.vue';
    import Tab from './components/Tab.vue';
    import Table from './components/Table.vue';

    export default {
        name: 'app',
        components: { TabNav, Tab, Table },
        data() {
            return {
                selected: ''
            }
        },
        methods: {
        setSelected(tab) {
            this.selected = tab;
        }
        }
    }
</script>

<style>
    #app {
        font-family: sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c2d50;
        margin-top: 60px;
        display: flex;
        flex-direction: row;
        justify-content: center;
    }
</style>