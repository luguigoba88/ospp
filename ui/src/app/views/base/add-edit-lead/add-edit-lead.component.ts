import {Component, Input, OnInit} from '@angular/core';
import {OsppService} from '../../../ospp.service';

@Component({
  selector: 'app-add-edit-lead',
  templateUrl: './add-edit-lead.component.html',
  styleUrls: ['./add-edit-lead.component.scss']
})
export class AddEditLeadComponent implements OnInit {

  constructor(private service: OsppService) { }

  @Input() gru: any;
  GroupsId: string;
  GroupName: string;

  ngOnInit(): void {
    this.GroupsId = this.gru.GroupsId;
    this.GroupName = this.gru.GroupName;
  }

  addGroup() {
    var val = {GroupsId: this.GroupsId,
                GroupName: this.GroupName};
    this.service.addGroup(val).subscribe(res => {
      alert(res.toString());
    });
  }

  updateGroup() {
    var val = {GroupsId: this.GroupsId,
      GroupName: this.GroupName};
    this.service.updateGroup(val).subscribe(res => {
    alert(res.toString());
    });
  }

}
