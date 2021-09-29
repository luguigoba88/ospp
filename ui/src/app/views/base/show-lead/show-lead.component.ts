import { Component, OnInit } from '@angular/core';
import {OsppService} from '../../../ospp.service';

@Component({
  selector: 'app-show-lead',
  templateUrl: './show-lead.component.html',
  styleUrls: ['./show-lead.component.scss']
})
export class ShowLeadComponent implements OnInit {

  constructor(private service: OsppService) { }

  GroupList: any = [];

  ModalTitle: string;
  ActivateAddEditGruComp: boolean = false;
  gru: any;

  GroupIdFilter: string = '';
  GroupNameFilter: string = '';
  GroupListWithoutFilter: any = [];

  ngOnInit(): void {
    this.refreshGruList();
  }

  addClick() {
    this.gru = {
      GroupsId: 0,
      GroupName: ''
    };
    this.ModalTitle = 'Agregar Grupo';
    this.ActivateAddEditGruComp = true;

  }

  editClick(item) {
    this.gru = item;
    this.ModalTitle = 'Editar Grupo';
    this.ActivateAddEditGruComp = true;
  }

  deleteClick(item) {
    if (confirm('Estas seguro??')) {
      this.service.deleteGroup(item.GroupsId).subscribe(data => {
        alert(data.toString());
        this.refreshGruList();
      });
    }
  }

  closeClick() {
    this.ActivateAddEditGruComp = false;
    this.refreshGruList();
  }


  refreshGruList() {
    this.service.getGruList().subscribe(data => {
      this.GroupList = data;
      this.GroupListWithoutFilter = data;
    });
  }

  FilterFn() {
    var GroupIdFilter = this.GroupIdFilter;
    var GroupNameFilter = this.GroupNameFilter;

    this.GroupList = this.GroupListWithoutFilter.filter(function (el) {
        return el.GroupsId.toString().toLowerCase().includes(
          GroupIdFilter.toString().trim().toLowerCase()
        ) &&
        el.GroupName.toString().toLowerCase().includes(
          GroupNameFilter.toString().trim().toLowerCase()
        );
    });
  }

  sortResult(prop, asc) {
    this.GroupList = this.GroupListWithoutFilter.sort(function(a, b) {
      if (asc) {
          return (a[prop] > b[prop]) ? 1 : ((a[prop] < b[prop]) ? -1 : 0);
      } else {
        return (b[prop] > a[prop]) ? 1 : ((b[prop] < a[prop]) ? -1 : 0);
      }
    });
  }

}
